const categories = document.querySelector(".categories");
const next = document.querySelector(".next");
const prev = document.querySelector(".prev");

next.addEventListener("click", function () {
    categories.scrollBy({
        left: -200,
        behavior: "smooth"
    });
});
prev.addEventListener("click", function () {
    categories.scrollBy({
        left: 200,
        behavior: "smooth"
    });
});
