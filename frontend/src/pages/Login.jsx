const Login = ({loginTrigger, endpoint}) => {

    const url = endpoint;
    const handleLogin = async (e) => {
        e.preventDefault();
        let inputEmail = e.target.parentElement.querySelector('#email').value;
        let inputPassword = e.target.parentElement.querySelector('#password').value;

        const loginObj = {
            httpMethod: "POST",
            action: "login",
            email: inputEmail,
            password: inputPassword
        }

        const response = await fetch(url, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(loginObj),
        });

        const data = await response.json();
        console.log(data)

        if (data != 'failed'){
            loginTrigger(data)
        }

    }

    return (
        <div>
            <form action="">
                <input type="text" placeholder="Email" id="email"/>
                <input type="text" placeholder="Password" id="password"/>
                <button onClick={handleLogin}>Log in</button>
            </form>

        </div>
    );
};

export default Login;
