import { useState } from "react";
import Login from "./Login";
import Main from "./Main";
import Register from "./Register";

const Wrapper = () => {

    const [currentUser, setCurrentUser] = useState([])

    // API endpoint
    const endpoint = "https://db137lkjma.execute-api.us-east-1.amazonaws.com/Testing/LambdaDB"

    const [registered, setRegistered] = useState(true);

    const loginTrigger = (userDetails) => {
        setCurrentUser(userDetails);
    }

    const switchToRegister = (e) => {
        e.preventDefault();
        setRegistered(false)
    }

    const switchToLogin = () => {
        setRegistered(true)
        setCurrentUser('')
    }


    return (
        <div>
            {
                registered ?
              (  currentUser == '' ?
              <div className="login-page">

                <Login loginTrigger={loginTrigger} endpoint={endpoint}/>
                <a href="" onClick={switchToRegister} className="register-link">Register</a>
              </div>
                :
                <Main currentUser={currentUser} endpoint={endpoint} logoutListener={switchToLogin}/>

            ) :
                <Register switchToLogin={switchToLogin} endpoint={endpoint}/>
            }

        </div>
    )
}

export default Wrapper;