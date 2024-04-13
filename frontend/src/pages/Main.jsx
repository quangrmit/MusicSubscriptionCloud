import Username from "../components/Username";
import TabsContainer from "../components/TabContainer";
import MusicRow from "../components/MusicRow";
import { useEffect, useState } from "react";

const Main = ({currentUser, endpoint}) => {
    const username = "to be replaced";

    const tabNames = ["My Music", "Search"];

    const contents = null;

    // const url = endpoint;
    const url = 'https://470yfgs920.execute-api.us-east-1.amazonaws.com/Testing/LambdaDBTest'

    const handleClick = async (e) => {
        e.preventDefault();
        let inputTitle = e.target.parentElement.querySelector("#title").value.trim();
        let inputYear = e.target.parentElement.querySelector("#year").value.trim();
        let inputArtist = e.target.parentElement.querySelector("#artist").value.trim();
        
        if (inputTitle == '' && inputYear == '' && inputArtist == ''){
            // notify user of error
            console.log('no parameters')
            return ;
        }
        let obj = {
            title  : inputTitle,
            year: inputYear,
            artist: inputArtist
        }

        let urlString = `${url}?`;

        for (const [key, value] of Object.entries(obj)){
            if (value != ''){
                urlString += `${key}=${value}&` 
            }
        }


        const response = await fetch(urlString, {
            method: "GET", 
            headers: {
                "Content-Type" : "application/json"
            },
        })

        const data = await response.json();

        const items = data;
        setMusicResult(items)
    };

    const [musicResult, setMusicResult] = useState([])

    const [subscribedSongs, setSubscribedSongs] = useState([])

    useEffect(()  => {
        const getSubscribed = async () => {
            
            let response = await fetch(`${url}?email=${currentUser[0]}`, {
                method: "GET",
                headers: {
                    "Content-Type": "application/json"
                }
            });
            
            const data = await response.json();
            console.log(data)
            setSubscribedSongs(data)
        }
        getSubscribed()
    }, [])


    const addSubscription = async (title) => {
        const obj = {
            httpMethod: "POST",
            action: "subscribe",
            email: currentUser[0],
            title: title
        }

        const response = await fetch(url, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(obj),
        });
        let data = await response.json();

        // should return the subscibed songs
        setSubscribedSongs(data)
    }



    return (
        <div className="main-page">
            <Username username={currentUser[1]} />
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
                { musicResult.length > 0 ?
                musicResult.map((item, index) => {
                    return (
                        <MusicRow key={index}
                            artist={item.artist}
                            title={item.title}
                            year={item.year}
                            addSubscription={addSubscription}
                            subscribed= {subscribedSongs.includes(item.title)}
                        />
                    )
                }) : <p>No music is found</p>
            }
            </div>
        </div>
    );
};

export default Main;
