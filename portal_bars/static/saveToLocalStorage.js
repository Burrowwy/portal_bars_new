function saveToLocalStorage() {
  var inputName = document.getElementById("name");
  var inputEmail = document.getElementById("email");
  var inputMessage = document.getElementById("message");
  localStorage.setItem(
    inputName.value,
    JSON.stringify({
      email: inputEmail.value,
      message: inputMessage.value,
    })
  );
}
