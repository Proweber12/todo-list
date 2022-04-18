import React from "react";

import {Link} from "react-router-dom";

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

            <Link to={`/projects/${project.id}`}>{project.name}</Link>

            <td>{project.link}</td>

            <td>{userList.join(', ')}</td>

        </tr>
    )
}

const ProjectList = ({projects, users}) => {

    return (
        <table>

            <th>Название</th>

            <th>Ссылка</th>

            <th>Участники</th>

            {projects.map((project) => <ProjectItem project={project} user={users}/>)}

        </table>
    )

}

export default ProjectList;