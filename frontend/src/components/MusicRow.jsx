const MusicRow = ({ title, year, artist, addSubscription, subscribed }) => {
    const handleSubscribe = () => {
        addSubscription(title);
    };

    return (
        <div>
            <li>
                artist: {artist}
                title: {title}
                year: {year}
                <img src={`https://s3927198-music-images.s3.amazonaws.com/${artist.split(' ').join('')}.jpg`} />
                {subscribed ? <p>Subscribed</p> : <button onClick={handleSubscribe}>Subscribe</button>}
            </li>
        </div>
    );
};

export default MusicRow;
