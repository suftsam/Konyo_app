function toggleChat() {
  var chatContainer = document.getElementById("chatContainer");
  chatContainer.style.display = chatContainer.style.display = "block";
}

function closeChat() {
  var chatContainer = document.getElementById("chatContainer");
  chatContainer.style.display = "none";
}

function sendMessage() {
  var messageInput = document.getElementById("messageInput");
  var message = messageInput.value;
  
  if (message !== "") {
    var chatBody = document.getElementById("chatBody");
    var newMessage = document.createElement("div");
    newMessage.classList.add("message");
    newMessage.innerText = message;
    chatBody.appendChild(newMessage);
    
    messageInput.value = "";
  }
}
