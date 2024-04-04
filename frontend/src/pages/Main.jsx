import Username from "../components/Username";
import TabsContainer from "../components/TabContainer";

const Main = () => {

    const username = "to be replaced";

    const tabNames = ['My Music', 'Search'];

    const contents = null;

    return (
        <div className="main-page">
            <Username username={username}/>
            <TabsContainer names={tabNames}/>
        </div>
    )
}

export default Main;