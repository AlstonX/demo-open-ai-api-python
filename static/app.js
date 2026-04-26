const form = document.querySelector("#chatForm");
const input = document.querySelector("#messageInput");
const messages = document.querySelector("#messages");
const emptyState = document.querySelector("#emptyState");
const sendButton = document.querySelector("#sendButton");
const clearButton = document.querySelector("#clearButton");

function setBusy(isBusy) {
  sendButton.disabled = isBusy;
  clearButton.disabled = isBusy;
  input.disabled = isBusy;
}

function updateEmptyState() {
  const hasMessages = messages.querySelector(".message");
  emptyState.hidden = Boolean(hasMessages);
}

function appendMessage(role, content) {
  const bubble = document.createElement("div");
  bubble.className = `message ${role}`;
  bubble.textContent = content;
  messages.appendChild(bubble);
  updateEmptyState();
  messages.scrollTop = messages.scrollHeight;
}

function renderHistory(history) {
  messages.querySelectorAll(".message").forEach((message) => message.remove());
  history.forEach((message) => appendMessage(message.role, message.content));
  updateEmptyState();
}

function autosizeInput() {
  input.style.height = "auto";
  input.style.height = `${input.scrollHeight}px`;
}

async function loadHistory() {
  const response = await fetch("/api/history");
  const data = await response.json();
  renderHistory(data.history || []);
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const message = input.value.trim();

  if (!message) {
    return;
  }

  appendMessage("user", message);
  input.value = "";
  autosizeInput();
  setBusy(true);

  try {
    const response = await fetch("/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message }),
    });
    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.error || "Request failed.");
    }

    renderHistory(data.history || []);
  } catch (error) {
    appendMessage("error", error.message);
  } finally {
    setBusy(false);
    input.focus();
  }
});

clearButton.addEventListener("click", async () => {
  setBusy(true);

  try {
    const response = await fetch("/api/clear", { method: "POST" });
    const data = await response.json();
    renderHistory(data.history || []);
  } catch (error) {
    appendMessage("error", error.message);
  } finally {
    setBusy(false);
    input.focus();
  }
});

input.addEventListener("input", autosizeInput);
input.addEventListener("keydown", (event) => {
  if (event.key === "Enter" && !event.shiftKey) {
    event.preventDefault();
    form.requestSubmit();
  }
});

loadHistory().catch((error) => appendMessage("error", error.message));
