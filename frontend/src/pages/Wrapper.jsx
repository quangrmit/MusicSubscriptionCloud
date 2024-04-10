import { useState } from "react";
import Login from "./Login";
import Main from "./Main";

const Wrapper = () => {

    const [currentUser, setCurrentUser] = useState('')

    const loginTrigger = (email) => {
        setCurrentUser(email);
    }

    return (
        <div>
            {
                currentUser == '' ?
                <Login loginTrigger={loginTrigger}/>
                :
                <Main currentUser={currentUser}/>
            }
        </div>
    )
}

export default Wrapper;