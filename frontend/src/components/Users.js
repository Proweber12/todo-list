import React from "react";

import {Link} from "react-router-dom";

const UserItem = ({user}) => {
    return (
        <tr>

            <Link to={`/users/${user.id}`}>{user.username}</Link>

            <td>{user.firstName}</td>

            <td>{user.lastName}</td>

            <td>{user.email}</td>

        </tr>
    )
}

const UserList = ({users}) => {

    return (
        <table>

            <th>Имя пользователя</th>

            <th>Имя</th>

            <th>Фамилия</th>

            <th>E-mail</th>

            {users.map((user) => <UserItem user={user}/>)}

        </table>
    )

}

export default UserList;