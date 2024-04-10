import Username from "../components/Username";
import TabsContainer from "../components/TabContainer";
import MusicRow from "../components/MusicRow";
import { useState } from "react";

const Main = ({currentUser}) => {
    const username = "to be replaced";

    const tabNames = ["My Music", "Search"];

    const contents = null;

    const url = "https://jhig1vzwx1.execute-api.us-east-1.amazonaws.com/Production/react-lambda-test";

    const handleClick = async (e) => {
        e.preventDefault();
        let title = e.target.parentElement.querySelector("#title").value.trim();
        let year = e.target.parentElement.querySelector("#year").value.trim();
        let artist = e.target.parentElement.querySelector("#artist").value.trim();

        if (title == '' && year == '' && artist == ''){
            // notify user of error
            console.log('no parameters')
            return ;
        }

    
        const searchObj = {
            type: "get",
            artist: artist,
            title: title, 
            year: year
        };

        const response = await fetch(url, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(searchObj),
        });

        const data = await response.json();
        if (!data){
            return ;
        }

        const items = data.body.items;
        setMusicList(items)

        console.log(data);
    };

    const [musicList, setMusicList] = useState([])

    return (
        <div className="main-page">
            <Username username={currentUser} />
            <TabsContainer names={tabNames} />

            <form action="">
                <input type="text" placeholder="Title" id="title" />
                <input type="text" placeholder="Year" id="year" />
                <input type="text" placeholder="Artist" id="artist" />

                <button onClick={handleClick} type="">
                    Test
                </button>
            </form>

            <div>
                { musicList.length > 0 ?
                musicList.map((item, index) => {
                    return (
                        <MusicRow key={index}
                            artist={item.artist}
                            title={item.title}
                            year={item.year}
                        />
                    )
                }) : <p>No music is found</p>
            }
            </div>
        </div>
    );
};

export default Main;
