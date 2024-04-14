import { useState } from "react";
import Login from "./Login";
import Main from "./Main";
import Register from "./Register";

const Wrapper = () => {

    const [currentUser, setCurrentUser] = useState([])

    // API endpoint
    const endpoint = "https://njycxyzj03.execute-api.us-east-1.amazonaws.com/Testing/LambdaDBTest"

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
    }

    return (
        <div>
            {
                registered ?
              (  currentUser == '' ?
              <div>

                <Login loginTrigger={loginTrigger} endpoint={endpoint}/>
                <a href="" onClick={switchToRegister}>Register</a>
              </div>
                :
                <Main currentUser={currentUser} endpoint={endpoint}/>

            ) :
                <Register switchToLogin={switchToLogin} endpoint={endpoint}/>
            }

        </div>
    )
}

export default Wrapper;