const btn = document.getElementById("theme-toggle");

btn.addEventListener("click", () => {

    document.body.classList.toggle("light");

});

const search = document.getElementById("search");

search.addEventListener("keyup", () => {

    let value = search.value.toLowerCase();

    let cards = document.querySelectorAll(".cert-card");

    cards.forEach(card => {

        let title = card.querySelector("h2")
            .textContent
            .toLowerCase();

        if(title.includes(value)){

            card.style.display = "block";

        } else {

            card.style.display = "none";

        }

    });

});