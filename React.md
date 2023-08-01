React component vs Element:

Component is a javascript class or function that returns elements
Element is what gets returned from components. 
it is an object that virtually describes the DOM nodes that a component represents.
with functional components element is the object returned by the function.
with class components element is the object returned by the render method.

____________________________

synthetic events : wrapper around the browser's native event. they combine the behaviour of different browsers into one API.
____________________________

useRef: ref is a value that is persisted in between re-renders and it doesnt cause the component to re-render.
the biggest use case for refs is to reference elements inside the html but setting the ref property on the elements
which should be avoided because we should let react take care of all the changes in re-render we should always use props
and state to update the component

usecases: save the previous value of a state variable
save the no of times a component is rendered
with html elements, we can use it to focus and animations
____________________________

HOC: it is a component that takes in another component as an input and returns an updated component
with new functionality addded to it.  it can also be used to have the repeated or duplicated code in one place
and can also be used to style the components in a consistent way.

function UpdatedComponent(OriginalComponent){
    function NewComponent(){
        const [money,setMoney] = useState(10);
        const handleIncrease = () =>{
            setMoney(money*2);
        }
        return <OriginalComponent handleIncreae={handleIncrease} money={money}>
    }
    return NewComponent;
}
export default UpdatedComponent;

function Person1({money,handleIncrease}){
    return (
        <div>
            <h2>{money}</h2>
            <button onClick={handleIncrease}>Increase money</button>
        </div>
    )
}
export default UpdatedComponent(Person1);
____________________________
pure component: renders the same output for the same state and props.
it also renders only when there is a change in its props
____________________________

React Router:
to configure routing in react, can be done in multiple ways
 using <Routes>:
    export function BookRoutes() {
        return (
            <Routes>
              <Route element={<BookLayout />}>
                  <Route index element={<BookList />} />
                  <Route path=":id" element={<Book />} />
                  <Route path="new" element={<NewBook />} />
                  <Route path="*" element={<NotFound />} />
              </Route>
            </Routes>
        )
    }

useRoutes:
    export function App() {
        const element = useRoutes([
            {
                path: "/",
                element: <Home />
            },
            {
                path: "/books",
                children: [
                    { index: true, element: <BookList /> },
                    { path: ":id", element: <Book /> }
                ]
            }
        ])
        return element
    }

    
import { BrowserRouter, Routes, Route } from "react-router-dom";
function App() {
  const isLoggedIn = useSelector(state => state.auth.isLoggedIn);

  const router = createBrowserRouter([
    {
      path: "/",
      element: !isLoggedIn ? <Login /> : <Navigate to="home" />,
      index: true
    },
    {
      path: "home",
      element: <Home />,
      children: [
        {
          index: true,
          element: <HabitsList />
        },
        {
          path: 'analytics',
          element: <Analytics></Analytics>
        }
      ]
    },
    {
      path: "*",
      element: <PageNotFound></PageNotFound>
    }
  ]);
  return (
    <RouterProvider router={router} />
  );
}

BrowserRouter: default router and is used 90% of use cases
NativeRouter: used in react native for routing
HashRouter: appends a # at the end of the domain name and before the path http://localhost:3000/#/books
HistoryRouter
MemoryRouter
StaticRouter

to naviagate we use <Link> and <NavLink> by setting the "to" property on these elements
<Link to="/books">Books</Link>
<NavLink
  to="/"
  style={({ isActive }) => ({ color: isActive ? "red" : "black" })}
>
NavLink allows us to style the Links dynamically

to manually navigate use the useNavigate() hook

____________________________
Controlled Component: the component that doesnt manage its own state and it recieves data from its parent as props is called
a controlled component. it only renders the props it recieved and doesnt maintain any state

UnControlled Components: the components that maintain their own state and doesnt depend on the parent component to set their state as via props
____________________________
mapStateToProps: allows the component to access the state in the store and update its props accrodingly.
____________________________

Hooks:

useMemo() : used to memoize a function or a object that needs to be changed only when the values it depends on needs to be changed.

const result = useMemo(() => {
  return slowFunction(a)
}, [a])

this slow function is invoked again only if there is a change in the a variable. earlier it used to run on every re-render causing the app to render slowly.

every time a component renders the objects are created again and they get a new reference
if there is a useeffect running based on this object it will cause the useeffect to run even if there is no change in 
the object internally to avoid this we need to memoise the object. so that the side effect runs only when the internal state of object changes

 const params = useMemo(() => {
    return { param1, param2, param3: 5 }
  }, [param1, param2])

  useEffect(() => {
    callApi(params)
  }, [params])


useCallback(): similar to useMemo() except that it works only with functions. it returns a function and usememo returns a value
____________________________

forwardRef: it is an higher order component that gets another parameter as an input along with the props
we use it when we want to control the DOM elements in the child component in the parent component


import { useRef, useEffect, forwardRef } from 'react'

export function Parent() {
  const elementRef = useRef()

  useEffect(() => {
    console.log(elementRef.current) // logs <div>Hello, World!</div>
  }, [])

  return <Child ref={elementRef} /> // assign the ref
}

const Child = forwardRef(function(props, ref) {
  return <div ref={ref}>Hello, World!</div>
})

you can also use it to access the methods in the child component in the parent component

import { useRef, forwardRef, useImperativeHandle } from 'react'

export function Main() {
  const methodsRef = useRef()

  const focus = () => methodsRef.current.focus()
  const blur = () => methodsRef.current.blur()

  return (
    <>
      <FocusableInput ref={methodsRef} />
      <button onClick={focus}>Focus input</button>
      <button onClick={blur}>Blur input</button>
    </>
  )
}

const FocusableInput = forwardRef(function (props, ref) {
  const inputRef = useRef()

  useImperativeHandle(ref, // forwarded ref
    function () {
      return {
        focus() { inputRef.current.focus() },
        blur() { inputRef.current.blur() }
      } // the forwarded ref value
    }, [])

  return <input type="text" ref={inputRef} />
})

here the focus and blur methods defined in the child component are passed back to the parent component
and these functions can be invoked via the ref that has been forwarded ref
____________________________
Error Bounday: 

Error boundary is used as part of the error handling process. it is a class component that implements two life cycle methods
namely.  
getDerivedStateFromError : used for updating the state of the component when an error raises
componentDidCatch : used for doing something specific when an error occurs, like add a log to server

the Error boundary wraps the other components as children and when there is a error it 
renders the fallback component that is passed to it as prop
if there is no error then it renders the children

class ErrorBounday extends React.component{
    state = { hasError:false }
    static getDerivedStateFromError(error){
        return { hasError:true }
    }
    componentDidCatch(){
        console.log(info)
    }
    render(){
        if(this.state.hasError){
            return this.props
        }
        return this.props.children
    }
}
export default ErrorBounday

<ErrorBoundary fallback="error loading component">
    <App/>
</ErrorBoundary>
____________________________
lazyloading: 
const OtherComponent = React.lazy(() => import('./OtherComponent'));

function MyComponent() {
  return (
    <div>
      <Suspense fallback={<div>Loading...</div>}>
        <OtherComponent />
      </Suspense>
    </div>
  );
}
____________________________
React.memo :

functional components re-render themselves every time the parent component re-renders even if their props dont change, to avoid 
this in class based components we have shouldComponentHook(), but in case of functional component we don't have these hooks available.
to achieve this we can use React.memo() to which we pass in the component and it recieves a new memoised component which only re-renders 
when the props have changed

const SomeComponent = (props) => (<div>HI</div>)
export default React.memo(SomeComponent)
____________________________
React fiber: 

it is a new rendering engine that makes rendering in react faster and smarter. it is the default rendering engine from react 16.
the previous reconcilation algorithms were using a synchronous approach. fiber takes an async approach with this react can pause, resume and restart rendering. 
with this react can also split work into chunk and prioritise tasks based on their importance.
____________________________

Life cycle methods:

  Mounting : these methods are called when a component is created and inserted into DOM
    constructor(props): 
      called when a component is created, 
      used to initialise state and bind event handlers
      dont cause side effects

    static getDerivedStateFromProps(props,state): 
      used when the state of the component depends on changes in props over time
      return a new object that represents the state of the component or return null
      since it is a static method, you cannot call this.setState
      dont cause side effects

    render():
      only required method in class component
      read props and state and return JSX
      dont update the state or make AJAX calls
      children components lifecycle methods are also executed after this
      
    componentDidMount():
      called only once in the entire lifecycle and it is invoked
      immediately after a component and all its children components have been rendered to the DOM
      you can cause side effects here by interacting with DOM nodes and making AJAX calls to load Data
      this is equivalent to calling useEffect with and empty dependency array

  Updating:
    static getDerivedStateFromProps(props,state):
      called every time a component is being re-rendered

    shouldComponentUpdate(newProps,newState):
      return true or false which will define if the component shoudl re-render or not
      you can compare current props, state with new Props, new state and decide if 
      component should update or not and helps us with performance optimisation

    render():

    getSnapShotBeforeUpdate(prevProps, prevState):
      called before the changes from the virtual DOM are to be reflected in the DOM
      used to capture some information from DOM
      this method will either return a null or a value which will be passed
      as the third parameter to the next method

    componentDidUpdate(prevProps, prevState, snapShot):
      called after the render is finished in the re-render cycles
      called when there is a change in state or component is re-evaluated
      it is equivalent to calling useEffect with a dependency array
      which means the component and all its child components have properly rendered
      after the update
      this method is called only once in a render cycle, hence we can cause side effects


  UnMounting:
    componentWillUnmount(): 
      similar to cleanup() in useEffect
      invoked immediately before the component is unmounted and destoryed
      you can perform clean up operations in this method

  ErrorHandling: these methods are called when there is an error in the component
  or in the child component and is used for creating error boundaries
    static getDerivedStateFromError()
    componentDidCatch()
____________________________
PureComponent: A pure component in React implements a shouldComponentUpdate with a
shallow comparison between prevState, currState and prevProps, currProps 

Pure components only re-render when there is a change in the state or props
and they give us a performance boost by avoiding unnecessary re-renders
____________________________

