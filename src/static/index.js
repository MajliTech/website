cache = {
    "null": "null"
}

function close() {
    document.querySelector("#header").style.display = "none"
    document.querySelector("#mobileMenu").style.display = null
    if (window.innerWidth > 770) {
        show()
    }
}
function uDShort(substring) {
    btn = document.querySelector('#' + substring)
    btn.style.backgroundColor = "var(--color)"
    content = document.querySelector("#content")
    content.childNodes.forEach(element => {
        element.remove()
    });
    if (!cache[substring] == undefined) {
        content.innerHTML = cache[substring]
    } else {
        const xhr = new XMLHttpRequest();
        xhr.open("GET", "/content/" + substring + ".html");
        xhr.onload = function () {
            if (xhr.status === 200) {
                cache[substring] = xhr.responseText
                content.innerHTML = xhr.responseText;
                const scriptElements = content.querySelectorAll('script[data-execute]');
                scriptElements.forEach(scriptElement => {
                    eval(scriptElement.innerText); // Execute the script content
                });
            } else {
                content.innerHTML = "<h1>Błąd wczytywania zawartości. <a href='https://github.com/MajliTech/website'>Chcesz to zgłośić?</a></h1>";
            }
        };
        xhr.send();

    }

}
function updateContent() {
    c = document.querySelector("#header").children
    for (let element of c) {
        if (element.classList.contains("btn")) {
            element.setAttribute("data-selected", "false")
            element.style.backgroundColor = null

        }
    }
    if (location.hash.substring(1) == "omnie") {
        uDShort("omnie")
    }
    else if (location.hash.substring(1) == "projekty") {
        uDShort("projekty")

    } else if (location.hash.substring(1) == "socialmedia") {
        uDShort("socialmedia")

    } else if (location.hash.substring(1) == "kontakt") {
        uDShort("kontakt")

    }
}
function show() {
    document.querySelector("#header").style.display = "flex"
    document.querySelector("#mobileMenu").style.display = "none"
}
document.addEventListener("DOMContentLoaded", () => {
    document.querySelector("#header").addEventListener("click", close)
    if (!location.hash.substring(1)) {
        location.hash = "omnie"
    }
    updateContent()
    window.addEventListener('resize', () => {

        if (window.innerWidth > 770) {
            show()
        }
    });
})