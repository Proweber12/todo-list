import React from "react";

const TodoItem = ({todo}) => {
    return (
        <tr>

            <td>{todo.text}</td>

            <td>{todo.create}</td>

            <td>{todo.update}</td>

            <td>{todo.isActive.toString()}</td>

            <td>{todo.creator}</td>

            <td>{todo.project}</td>

        </tr>
    )
}

const TodoList = ({todos}) => {

    return (
        <table>

            <th>Текст</th>

            <th>Создано</th>

            <th>Обновлено</th>

            <th>Активность</th>

            <th>Создатель</th>

            <th>Проект</th>

            {todos.map((todo) => <TodoItem todo={todo}/>)}

        </table>
    )

}

export default TodoList;