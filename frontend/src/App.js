import React from 'react';
import axios from "axios";
import Cookies from "universal-cookie";
import './App.css';

import Menu from "./components/Menu";
import Footer from "./components/Footer";
import UserList from "./components/Users";
import ProjectList from "./components/Projects";
import ProjectListUsers from "./components/UserProjects";
import ProjectDetail from "./components/ProjectDetail";
import TodoList from "./components/Todos";
import NotFound404 from "./components/NotFound404";
import LoginForm from "./components/Auth";
import {Route, BrowserRouter, Switch, Link} from "react-router-dom";


class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'users': [],
            'projects': [],
            'todos': [],
            'access_token': '',
            'refresh_token': '',
            'username': '',
        }
    }

    load_data(){
        const headers = this.get_headers()

        axios.get('http://127.0.0.1:8000/api/users/0.1/', {headers}).then(response => {
                this.setState(
                    {
                        "users": response.data.results
                    }
                )
            }
        ).catch(error =>
            {
                if(error.response.status === 401 && !!this.state.access_token) {
                        axios.post('http://127.0.0.1:8000/api-token-auth/refresh/',
                        {'refresh': new Cookies().get('refresh')})
                        .then(response => {
                        this.set_token(response.data['access'], new Cookies().get('refresh'), new Cookies().get('username'))
                        }
                    )
                }
            }
        )

        axios.get('http://127.0.0.1:8000/api/projects/', {headers}).then(response => {
                this.setState(
                    {
                        "projects": response.data.results
                    }
                )
            }
        ).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/todo/', {headers}).then(response => {
                this.setState(
                    {
                        "todos": response.data.results
                    }
                )
            }
        ).catch(error => console.log(error))
    }

    set_token(access_token, refresh_token, username) {
        const cookies = new Cookies()
        cookies.set('access', access_token)
        cookies.set('refresh', refresh_token)
        cookies.set('username', username)
        this.setState(
            {
                'access_token': access_token,
                'refresh_token': refresh_token,
                'username': username,
            }, () => this.load_data()
        )
        location.href = "/"
    }

    get_token(username, password) {
        axios.post('http://127.0.0.1:8000/api-token-auth/', {'username': username, 'password': password})
            .then(response => {
                this.set_token(response.data['access'], response.data['refresh'], username)
            }
        ).catch(() => alert("Введён неверный логин или пароль"))
    }

    is_auth() {
        return !!this.state.access_token;
    }

    get_headers() {
        let headers = {
            'Content-Type': 'applications/json'
        }

        if(this.is_auth()) {
            headers['Authorization'] = `Bearer ${this.state.access_token}`
        }

        return headers
    }

    logout() {
        this.set_token('', '', '')
        location.href = "/"
    }

    get_token_from_cookies() {
        const cookies = new Cookies()
        const access_token = cookies.get('access')
        this.setState(
            {
                'access_token': access_token,
            }, () => this.load_data()
        )
    }

    componentDidMount() {
        this.get_token_from_cookies()
    }

    render() {
        return (
            <div>
                <BrowserRouter>
                    <header>
                        <div className="menu">
                            <ul>
                                <Menu/>
                                {this.is_auth()?
                                <li>
                                    <Link to="/users">{new Cookies().get('username')}</Link>
                                    <div></div>
                                </li>: null
                                }
                                <li>
                                    {this.is_auth()? <Link onClick={() => this.logout()}>Выйти</Link>:
                                        <Link to="/login"> Регистрация/Вход</Link>}
                                    <div></div>
                                </li>
                            </ul>
                        </div>
                    </header>
                    <Switch>
                        <Route exact path='/' component={() => <TodoList projects={this.state.projects} users={this.state.users} todos={this.state.todos}/>}/>
                        <Route exact path='/users' component={() => <UserList users={this.state.users}/>}/>
                        <Route exact path='/users/:id' component={() => <ProjectListUsers users={this.state.users} projects={this.state.projects}/>}/>
                        <Route exact path='/projects' component={() => <ProjectList users={this.state.users} projects={this.state.projects}/>}/>
                        <Route exact path='/projects/:id' component={() => <ProjectDetail users={this.state.users} projects={this.state.projects}/>}/>

                        <Route exact path='/login' component={() => <LoginForm get_token={(username, password) => this.get_token(username, password)}/>}/>

                        <Route component={NotFound404}/>
                    </Switch>
                </BrowserRouter>
                <Footer/>
            </div>
        );
    }
}

export default App;
