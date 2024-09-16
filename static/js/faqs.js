var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function () {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.maxHeight) {
      content.style.maxHeight = null;
    } else {
      content.style.maxHeight = content.scrollHeight + "px";
    }
  });
}

document.querySelectorAll(".update-btn").forEach((button) => {
  button.addEventListener("click", function () {
    var id = this.getAttribute("data-id");
    var faq = document.querySelectorAll(".faq")[id];
    var question = faq.querySelector(".collapsible").innerText;
    var answer = faq.querySelector(".content p").innerText;

    document.getElementById("form-title").innerText = "Update Question";
    document.getElementById("faq-id").value = id;
    document.getElementById("question").value = question;
    document.getElementById("answer").value = answer;
    document.getElementById("submit-btn").innerText = "Update Question";
  });
});

document.querySelectorAll(".delete-btn").forEach((button) => {
  button.addEventListener("click", function () {
    var id = this.getAttribute("data-id");
    if (confirm("Are you sure you want to delete this FAQ?")) {
      fetch(`/faqs/${id}`, {
        method: "DELETE",
      }).then((response) => {
        if (response.ok) {
          location.reload();
        } else {
          alert("Failed to delete FAQ");
        }
      });
    }
  });
});
