import React, { useState } from 'react';
import { BrowserRouter as Router, Switch, Route, Link } from 'react-router-dom';
import { Container, Navbar, Nav, Button, Form, FormControl, ListGroup } from 'react-bootstrap';
import './App.css';

const App = () => {
  const [todos, setTodos] = useState([]);
  const [inputText, setInputText] = useState('');

  const handleInputChange = (e) => {
    setInputText(e.target.value);
  };

  const handleAddTodo = () => {
    if (inputText !== '') {
      const newTodo = {
        id: Date.now(),
        text: inputText,
      };

      setTodos([...todos, newTodo]);
      setInputText('');
    }
  };

  const handleDeleteTodo = (id) => {
    const updatedTodos = todos.filter((todo) => todo.id !== id);
    setTodos(updatedTodos);
  };

  return (
    <Router>
      <Navbar bg="dark" variant="dark">
        <Navbar.Brand as={Link} to="/">Todo List</Navbar.Brand>
        <Nav className="mr-auto">
          <Nav.Link as={Link} to="/">Home</Nav.Link>
          <Nav.Link as={Link} to="/todos">Todos</Nav.Link>
        </Nav>
      </Navbar>

      <Container className="mt-4">
        <Switch>
          <Route path="/" exact>
            <h1>Welcome to Todo List App!</h1>
          </Route>
          <Route path="/todos">
            <h2>Todos</h2>

            <Form inline className="mb-3">
              <FormControl type="text" placeholder="Enter a todo" value={inputText} onChange={handleInputChange} />
              <Button variant="primary" onClick={handleAddTodo}>Add</Button>
            </Form>

            <ListGroup>
              {todos.map((todo) => (
                <ListGroup.Item key={todo.id}>
                  {todo.text}
                  <Button variant="danger" size="sm" className="float-right" onClick={() => handleDeleteTodo(todo.id)}>Delete</Button>
                </ListGroup.Item>
              ))}
            </ListGroup>
          </Route>
        </Switch>
      </Container>
    </Router>
  );
};

export default App;
