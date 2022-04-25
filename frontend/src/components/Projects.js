import React from "react";

import {Link} from "react-router-dom";

const ProjectItem = ({project, user, deleteProject}) => {

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

            <td><button onClick={() => deleteProject(project.id)} type="button">УДАЛИТЬ</button></td>

            <td><Link to={`/projects/change/${project.id}`}>ИЗМЕНИТЬ</Link></td>

        </tr>
    )
}

const ProjectList = ({projects, users, deleteProject}) => {

    return (

        <main>

            <h1>Проекты</h1>

            <table>

                <th>Название</th>

                <th>Ссылка</th>

                <th>Участники</th>

                <th>Удаление</th>

                <th>Изменение</th>

                {projects.map((project) => <ProjectItem project={project} user={users} deleteProject={deleteProject}/>)}

            </table>

            <Link to='/projects/create' className='create'>Создать проект</Link>

            <Link to='/projects/find' className='find'>Найти проект</Link>

        </main>

    )

}

export default ProjectList;