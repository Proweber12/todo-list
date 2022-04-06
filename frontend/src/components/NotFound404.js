import React from "react";

const NotFound404 = ({location}) => {
    return (
            <div className="not_found_404">
                <h1 className="not_found_404__h1">Страница не найдена</h1>
                <img src="img/PageNotFound.jpg" className="not_found_404__img" alt=""/>
            </div>
    )
}

export default NotFound404;