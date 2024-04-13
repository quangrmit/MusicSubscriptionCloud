const Login = ({loginTrigger, endpoint}) => {

    const url = 'https://470yfgs920.execute-api.us-east-1.amazonaws.com/Testing/LambdaDBTest'

    

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
        loginTrigger(data)

    }

    return (
        <div>
            <form action="">
                <input type="text" placeholder="Email" id="email"/>
                <input type="text" placeholder="Password" id="password"/>
                <button onClick={handleLogin}>Log in</button>
            </form>
            <a href="">Register</a>
        </div>
    );
};

export default Login;
