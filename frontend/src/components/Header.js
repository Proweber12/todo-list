import React from "react";

import {Link} from "react-router-dom";

const Header = () => {
    return (
        <header>

            <div className="menu">
                <ul>
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
                    <li>
                        <Link to="/">Регистрация/Вход</Link>
                        <div></div>
                    </li>
                </ul>
            </div>

        </header>
    )
}

export default Header;