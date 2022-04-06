import React from "react";

import {Link} from "react-router-dom";

const ProjectItem = ({project}) => {
    return (
        <tr>

            <Link to={`/projects/${project.id}`}>{project.name}</Link>

            <td>{project.link}</td>

            <td>{project.users}</td>

        </tr>
    )
}

const ProjectList = ({projects}) => {

    return (
        <table>

            <th>Название</th>

            <th>Ссылка</th>

            <th>Участники</th>

            {projects.map((project) => <ProjectItem project={project}/>)}

        </table>
    )

}

export default ProjectList;