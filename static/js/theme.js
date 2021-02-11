const btn = document.querySelector(".btn-toggle");

btn.addEventListener("click", function () {
  document.body.classList.toggle("dark-theme");
});

function themeFunction() {
    var element = document.getElementsByClass("badge-light");
    element.classList.toggle("badge-dark");
  }

  $("a").click(function(){
    $("span").toggleClass("main");
  });