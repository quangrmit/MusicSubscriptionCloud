import { useState } from "react";
import Login from "./Login";
import Main from "./Main";

const Wrapper = () => {

    const [currentUser, setCurrentUser] = useState('')

    // API endpoint
    const endpoint = ""

    const loginTrigger = (email) => {
        setCurrentUser(email);
    }

    return (
        <div>
            {
                currentUser == '' ?
                <Login loginTrigger={loginTrigger} endpoint={endpoint}/>
                :
                <Main currentUser={currentUser} endpoint={endpoint}/>
            }
        </div>
    )
}

export default Wrapper;