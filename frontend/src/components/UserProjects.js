import React from "react";
import {useParams} from "react-router-dom";

const ProjectItem = ({project, user}) => {

    let userList = [];
    for (let i of user) {
        for (let j of project.users){
            if (i.id === j) {
            userList.push(i.username);
            break;
            }
        }
    }

    return (
        <tr>

            <td>{project.id}</td>

            <td>{project.name}</td>

            <td>{project.link}</td>

            <td>{userList.join(', ')}</td>

        </tr>
    )

}

const ProjectListUsers = ({projects, users}) => {
    let {id} = useParams()

    let filter_item = projects.filter((project => project.users.includes(Number(id))))

    return (

        <main>

            <h1>Проекты выбранного пользователя</h1>

            <table>

                <th>Id проекта</th>

                <th>Название</th>

                <th>Ссылка</th>

                <th>Участники</th>

                {filter_item.map((project) => <ProjectItem project={project} user={users}/>)}

            </table>

        </main>
    )

}

export default ProjectListUsers;