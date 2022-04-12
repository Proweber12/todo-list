import React from "react";
import {Link} from "react-router-dom";

const Menu = () => {
    return (
        <div>
            <li>
                <Link to="/">TODO</Link>
                <div></div>
            </li>
            <li>
                <Link to="/projects">Проекты</Link>
                <div></div>
            </li>
            <li>
                <Link to="/users">Все пользователи</Link>
                <div></div>
            </li>
        </div>
    )
}

export default Menu;