import { useState } from "react";

const NAMES = ["Tab 1", "Tab 2", "Tab 3"];
const CONTENTS = [<div>1</div>, <div>2</div>, <div>3</div>];

const TabsContainer = ({ names = NAMES, contents = CONTENTS }) => {
    const [currIndex, setCurrIndex] = useState(0);

    const handleSwitchTab = (index) => {
        setCurrIndex(index);
    };

    return (
        <div className="tab-container">
            {names.map((name, index) => {
                return <button key={index} onClick={() => handleSwitchTab(index)}>{name}</button>;
            })}

            {contents[currIndex]}
        </div>
    );
};

export default TabsContainer;
