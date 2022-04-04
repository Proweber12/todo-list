import React from "react";

const ProjectItem = ({project}) => {
    return (
        <tr>

            <td>{project.name}</td>

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