import React from 'react';
import axios from "axios";
import './App.css';

import Header from "./components/Header";
import Footer from "./components/Footer";
import UserList from "./components/Users";
import ProjectList from "./components/Projects";
import ProjectListUsers from "./components/UserProjects";
import ProjectDetail from "./components/ProjectDetail";
import TodoList from "./components/Todos";
import NotFound404 from "./components/NotFound404";
import {Route, BrowserRouter, Switch} from "react-router-dom";


class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'users': [],
            'projects': [],
            'todos': [],
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/users/').then(response => {
                this.setState(
                    {
                        "users": response.data.results
                    }
                )
            }
        ).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/projects/').then(response => {
                this.setState(
                    {
                        "projects": response.data.results
                    }
                )
            }
        ).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/todo/').then(response => {
                this.setState(
                    {
                        "todos": response.data.results
                    }
                )
            }
        ).catch(error => console.log(error))
    }

    render() {
        return (
            <div>
                <BrowserRouter>
                    <Header/>
                    <Switch>
                        <Route exact path='/' component={() => <TodoList todos={this.state.todos} users={this.state.users}/>}/>
                        <Route exact path='/users' component={() => <UserList users={this.state.users}/>}/>
                        <Route exact path='/projects' component={() => <ProjectList projects={this.state.projects}/>}/>

                        <Route exact path='/users/:id' component={() => <ProjectListUsers projects={this.state.projects}/>}/>
                        <Route exact path='/projects/:id' component={() => <ProjectDetail projects={this.state.projects}/>}/>

                        <Route component={NotFound404}/>
                    </Switch>
                </BrowserRouter>
                <Footer/>
            </div>
        );
    }
}

export default App;
