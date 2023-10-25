const button = document.getElementById("butn");
button.addEventListener("click", function() {
  button.style.backgroundColor = "#ff0000";
  button.style.color = "#000";
  setTimeout(function() {
    button.style.backgroundColor = "#007bff"; 
  }, 1000);
});
const buttonn = document.getElementById("butnn");
buttonn.addEventListener("click", function() {
  buttonn.style.backgroundColor = "#ff0000";
  buttonn.style.color = "#000";
  setTimeout(function() {
    buttonn.style.backgroundColor = "#007bff"; 
  }, 1000);
});
