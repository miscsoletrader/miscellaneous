const themebtn = document.getElementById('theme');
const sectionbg = document.body;

toggle.addEventListener('input', e => {
    const isChecked = e.target.checked;

    if (isChecked) {
        body.classList.add('dark');
    } else {
        body.classList.remove('dark');
    }
});

// function myFunction() {
//   var themebtn = document.getElementById("theme");

//   var sectionbg = document.getElementByClass("section-bg")

//   if ()
// }