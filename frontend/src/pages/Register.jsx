
const Register = () => {

    const handleRegister = async (e) => {
        e.preventDefault();
        let inputEmail = e.target.parentElement.querySelector('#email').value.trim();
        let inputUsername = e.target.parentElement.querySelector('#username').value.trim();
        let inputPassword = e.target.parentElement.querySelector('#password').value.trim();

        let obj = {
            httpMethod: "POST",
            action: "register",
            email: inputEmail,
            username: inputUsername,
            password: inputPassword
        }
        const url = 'https://470yfgs920.execute-api.us-east-1.amazonaws.com/Testing/LambdaDBTest'

        const response = await fetch(url, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(obj),
        });

        const data = await response.json();
        if (data == 'success'){
            // Redirect to login page
        }else{
            // Notify the user of the duplicated email
        }

        console.log(data)
    }

    return (
        <div>
            <form action="">
                <input type="text" placeholder="Email" id="email" />
                <input type="text" placeholder="Username" id="username"  />
                <input type="text" placeholder="Password" id="password" />

                <button onClick={handleRegister}>Register</button>
            </form>
        </div>
    )
}

export default Register