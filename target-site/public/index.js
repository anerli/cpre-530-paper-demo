console.log("This is the target site");


function login() {
    console.log("Logging In");

    //fetch("http://localhost:8000/login")

    let usernameInput = document.getElementById("usernameInput");
    let username = usernameInput.value;

    console.log("Provided username:", username);
    usernameInput.value = "";

    fetch(
        "http://localhost:8000/api/login/" + username,
        {
            // CORS mode
            mode: "same-origin",
            // Must be set to "include" or "same-origin" to send OR receive cookies
            credentials: "same-origin"
        }
    ).then(
        response => {
            console.log(response);
            return response.json()
        }
    ).then(
        data => {
            console.log(data);
            console.log(data.funds)
            fundsElement = document.getElementById("funds");
            console.log(fundsElement);
            console.log(fundsElement.textContent);
            fundsElement.textContent = data.funds.toString();
        }
    )
}