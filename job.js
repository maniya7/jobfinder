
// اسلایدر دسته‌بندی‌ها

const categories = document.querySelector(".categories");
const next = document.querySelector(".next");
const prev = document.querySelector(".prev");

if (categories && next && prev) {

    function updateArrows() {
        const maxScroll = categories.scrollWidth - categories.clientWidth;
        const position = Math.abs(categories.scrollLeft);

        prev.classList.toggle("is-hidden", position <= 1);
        next.classList.toggle("is-hidden", position >= maxScroll - 1);
    }

    next.addEventListener("click", function () {
        categories.scrollBy({
            left: -240,
            behavior: "smooth"
        });
    });

    prev.addEventListener("click", function () {
        categories.scrollBy({
            left: 240,
            behavior: "smooth"
        });
    });

    categories.addEventListener("scroll", updateArrows);
    window.addEventListener("resize", updateArrows);

    updateArrows();
}


// اطلاعات نمونه فرصت‌های شغلی

const jobs = [
    {
        title: "کارآموز فرانت‌اند",
        company: "شرکت فناوری نوین",
        category: "programming",
        city: "tehran",
        type: "internship"
    },
    {
        title: "طراح رابط کاربری UI/UX",
        company: "استودیو خلاق",
        category: "design",
        city: "qazvin",
        type: "freelance"
    },
    {
        title: "برنامه‌نویس JavaScript",
        company: "توسعه‌گران وب",
        category: "programming",
        city: "karaj",
        type: "fulltime"
    },
    {
        title: "کارشناس بازاریابی",
        company: "گروه بازرگانی آریا",
        category: "marketing",
        city: "isfahan",
        type: "parttime"
    },
    {
        title: "طراح گرافیک",
        company: "آژانس تبلیغاتی",
        category: "design",
        city: "remote",
        type: "freelance"
    }
];


// دریافت عناصر فرم

const searchForm = document.getElementById("jobSearchForm");
const keywordInput = document.getElementById("jobKeyword");
const categorySelect = document.getElementById("jobCategory");
const citySelect = document.getElementById("jobCity");
const typeSelect = document.getElementById("jobType");
const resultsContainer = document.getElementById("searchResults");


// جستجوی فرصت‌ها

if (searchForm && resultsContainer) {

    searchForm.addEventListener("submit", function (event) {

        event.preventDefault();

        const keyword = keywordInput.value.trim().toLowerCase();
        const selectedCategory = categorySelect.value;
        const selectedCity = citySelect.value;
        const selectedType = typeSelect.value;

        const filteredJobs = jobs.filter(function (job) {

            const matchesKeyword =
                job.title.toLowerCase().includes(keyword) ||
                job.company.toLowerCase().includes(keyword);

            const matchesCategory =
                selectedCategory === "all" ||
                job.category === selectedCategory;

            const matchesCity =
                selectedCity === "all" ||
                job.city === selectedCity;

            const matchesType =
                selectedType === "all" ||
                job.type === selectedType;

            return matchesKeyword &&
                matchesCategory &&
                matchesCity &&
                matchesType;

        });


        // نمایش نتایج

        resultsContainer.innerHTML = "";

        if (filteredJobs.length === 0) {

            resultsContainer.innerHTML = `
                <p class="no-results">
                    فرصتی با این مشخصات پیدا نشد.
                </p>
            `;

            return;
        }


        filteredJobs.forEach(function (job) {

            const jobCard = document.createElement("div");

            jobCard.classList.add("job-card");

            jobCard.innerHTML = `
                <h3>${job.title}</h3>
                <p>${job.company}</p>
                <p>${job.city}</p>
                <p>${job.type}</p>
            `;

            resultsContainer.appendChild(jobCard);

        });

    });

}
