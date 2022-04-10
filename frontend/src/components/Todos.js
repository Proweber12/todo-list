import React from "react";

const TodoItem = ({todo, users, projects}) => {
    let todo_create_date = todo.create.split('T')[0];
    let todo_create_time = todo.create.split('T')[1].split('.')[0];

    let todo_update_date = todo.update.split('T')[0];
    let todo_update_time = todo.update.split('T')[1].split('.')[0];

    let project = '';
    for (let i of projects) {
        if (i.id === todo.project) {
            project = i.name;
            break;
        }
    }

    let user = '';
    for (let j of users) {
        if (j.id === todo.creator) {
            user = j.username;
            break;
        }
    }

    return (
        <tr>

            <td>{todo.text}</td>

            <td>{`${todo_create_date}-${todo_create_time}`}</td>

            <td>{`${todo_update_date}-${todo_update_time}`}</td>

            <td>{todo.isActive.toString() === 'true'? '✅': '❌'}</td>

            <td>{user}</td>

            <td>{project}</td>

        </tr>
    )
}

const TodoList = ({todos, users, projects}) => {

    return (
        <table>

            <th>Текст</th>

            <th>Создано</th>

            <th>Обновлено</th>

            <th>Активность</th>

            <th>Создатель</th>

            <th>Проект</th>

            {todos.map((todo) => <TodoItem todo={todo} projects={projects} users={users}/>)}

        </table>
    )

}

export default TodoList;