const MyMusicRow = ({ title, year, artist, removeSong}) => {

    const deleteSong = () => {
        removeSong(title)
    }

    return (
        <div>
            <li>
                artist: {artist}
                title: {title}
                year: {year}
                <img src="https://s3927198-music-images.s3.amazonaws.com/ArcadeFire.jpg" alt="artist image" />
                <button onClick={deleteSong}>Remove</button>
            </li>
        </div>
    );
};

export default MyMusicRow;
