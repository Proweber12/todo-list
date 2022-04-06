import React from "react";
import {useParams} from "react-router-dom";

const ProjectItem = ({project}) => {

    return (
        <tr>

            <td>{project.id}</td>

            <td>{project.name}</td>

            <td>{project.link}</td>

            <td>{project.users}</td>

        </tr>
    )

}

const ProjectListUsers = ({projects}) => {
    let {id} = useParams()

    let filter_item = projects.filter((project => project.users.includes(Number(id))))

    return (
        <table>

            <th>Id</th>

            <th>Имя</th>

            <th>Ссылка</th>

            <th>Участники</th>

            {filter_item.map((project) => <ProjectItem project={project}/>)}

        </table>
    )

}

export default ProjectListUsers;