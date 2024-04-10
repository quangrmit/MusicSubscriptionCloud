const MusicRow = ({ title, year, artist }) => {
    return (
        <div>
            <li>
                artist: {artist}
                title: {title}
                year: {year}
                <img src="https://s3927198-music-images.s3.amazonaws.com/ArcadeFire.jpg" alt="artist image" />
                <button>Subscribe</button>
            </li>
        </div>
    );
};

export default MusicRow;