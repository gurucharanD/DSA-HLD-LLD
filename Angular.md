const observable1 = new Observable((observer: any) => {
    observer.next('I am Observable 1');
});
const observable2 = new Observable((observer: any) => {
    observer.next('I am Observable 2');
});

// merge
const observable3 = merge(observable1, observable2);
observable3.subscribe(data => console.log(data));
______________________________________
// of
of(1, 2, 3).subscribe(data => console.log(data));
______________________________________
// map
of('my name is lotanna')
    .pipe(
        map(data => data.toUpperCase()),
        map(data => data.toLowerCase())
    )
    .subscribe(data => console.log(data));
______________________________________
// from event
fromEvent(document, 'click').subscribe(() =>
    console.log('You clicked the page!')
);
______________________________________
// pluck
from([
    { brand: 'iPhone', model: 'Xmax', price: '$1000' },
    { brand: 'Samsung', model: 'S10', price: '$850' }
])
    .pipe(pluck('price'))
    .subscribe(data => console.log(data));
______________________________________
// take
fromEvent(document, 'click')
    .pipe(take(2))
    .subscribe(() => console.log('You clicked the page on take!'));
______________________________________
below operators are used when we have to pass the result of one observable into another observable and 
we want to avoid the usage of nested .subscribe calls these operators are called flattening operators

// mergemap
    when values are being emitted from the first observable, merge map waits for all the values to be emitted from first observable
    and then invokes the second observable in parallel, so the output from final Observable will not match the order in which the values are emitted from the intermediate observables

    let postIds = interval(1).pipe(
        filter(() => value > 0),
        take(5)
    )

    postIds.pipe(
        mergeMap((id) => {
            return this.hhtp.get(`https://jsonplaceholder.typicode.com.posts/{id}`)
        })
    ).subscribe((data) => {
        console.log(data)
    })

    all the http get calls to json api are made in parallel and which over call resolves first will be passed to next observable hence the order of data cannot be guaranteed

// concatmap
    when values are being emitted from the first observable, concatmap whenever it recievs a value from the first observable
    it passes it down to the next observable and it invokes second observable in series hence the order in which the result is 
    produced can be guaranteed

    let postIds = interval(1).pipe(
        filter(() => value > 0),
        take(5)
    )

    postIds.pipe(
        concatMap((id) => {
            return this.hhtp.get(`https://jsonplaceholder.typicode.com.posts/{id}`)
        })
    ).subscribe((data) => {
        console.log(data)
    })
    
    as soon as the concatMap recieves a value it sends a request to the JSON api


// switchmap
    when a values are being emitted from the first observable, when a new value is emitted by the first observable switchmap cancels the operation it is performing and starts processing the observable based on the new value

    let postIds = interval(1).pipe(
        filter(() => value > 0),
        take(5)
    )

    postIds.pipe(
        switchMap((id) => {
            return this.hhtp.get(`https://jsonplaceholder.typicode.com.posts/{id}`)
        })
    ).subscribe((data) => {
        console.log(data)
    })

    at the begining 1 is passed to the json api, while this is being processed value 2 is emitted hence the first api call with 1 
    is cancelled and it makes a new request with 2. this process continues until all the values are emitted from the first Observable
    
// exhaustmap
    when values are being emitted from the first observable, when a new value is emitted by the first observable exhaustMap if it has finished processing the value that has been emitted by the observable completely and if it is free only then it will process the new value if it still processing the previous value then it will ignore the new value. this process continues until all the values are finished processing

    let postIds = interval(1).pipe(
        filter(() => value > 0),
        take(5)
    )

    postIds.pipe(
        exhaustMap((id) => {
            return this.hhtp.get(`https://jsonplaceholder.typicode.com.posts/{id}`)
        })
    ).subscribe((data) => {
        console.log(data)
    })
______________________________________

Routing
normal route:
{ path:  'contacts', component:  ContactListComponent}

route with param:
{ path:  'contacts/:id', component:  ContactDetailComponent}

route with Guard:
{ path:  'contacts/:id, canActivate:[MyGuard], component:  ContactDetailComponent}
class MyGuard implements CanActivate {
  canActivate() {
    return true;
  }
}

<a [routerLink]="'/contacts'">Contacts</a>
______________________________________

multiple outlets:
<router-outlet></router-outlet>  
<router-outlet  name="outlet1"></router-outlet> 
{ path: "contacts", component: ContactListComponent, outlet: "outlet1" }

______________________________________

import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

const routes: Routes = [
    { path:  'contacts', component:  ContactListComponent},
    { path:  'contacts/:id', component:  ContactDetailComponent},
    { path: "contacts", component: ContactListComponent, outlet: "outlet1" }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
______________________________________
ActivatedRoute: 
use activatedRoute to get access to the route params passed as part of the URL

export class ContactDetailComponent implements OnInit {

  contact: any;
  constructor(private contactService: ContactService, private route: ActivatedRoute) { }

  ngOnInit() {
    this.route.paramMap.subscribe(params => {
    console.log(params.get('id'))
        this.contactService.getContact(params.get('id')).subscribe(c =>{
            console.log(c);
            this.contact = c;
        });   
    });
  }
}
______________________________________

Directives:

directives are classes that add new behavior or modify the existing behaviour of the elements in the template and DOM by adding, hiding, adding extra behaviour.
types:
    component: every component is a directive in angular
    structural: 
        used to change DOM structure by adding or removing
        elements. they are preceded by * 
        *ngIf, *ngFor, *ngSwitch
    attribute:
        change the appearence or behaviour of element
        ngStyle, ngClass

to create a custom directive create a class and decorate it with

@Directive({
    selector:'[DirectiveName]'
})
export class HighLightDirective{
    <!-- the element ref of the element using this directive 
    is injected into the component -->
    constructor(private eleRef:ElementRef){}
    <!-- you can access the events that are happening on the element
    by using @HostListener('eventName') method(){} syntax -->
}

to create strucutural directives we need 
ViewContainerRef: reference to the host element that hosts the component
TemplateRef: reference to the ng-template using the directive

ngOnChanges() {
  if (this.toggle) {
     this.viewRef.createEmbeddedView(this.tempRef);
  } else {
     this.viewRef.clear();
  }
}
______________________________________

Pipes: pipe is a function that we can apply on a value in a template and transform into another value.
types:
    pure pipe: doesn't run on every change detection cycle only runs when the input parameters are changed
    impure pipe: runs on every change detection cycle irrespective of the change in input parameter
when creating a pipe we can configure if it can be a pure or impure pipe

built in pipes:
    currency, date, decimal, json, lowercase, uppercase, percentage, slice, async
    async pipe: prints the value returned by a promise or an observable without 
    subscribing or resolving it
    json pipe: prints a json as a string on the DOM

    we can chain multiple pipes using the | opertaor
    {{ amount | decimal | pipe }}

To create a custom pipe create a class that implements pipeTransform and decorate it with 
@Pipe() and pass in the configuration

@Pipe({
    name:'my-pipe'
    pure:true
})
export class MyPipe implements PipeTransform{
    transform(value){
        return value+2
    }
}
______________________________________

Modules: Angular modules is a mechanism to group components, directives, pipes and services
that are related in such a way that can be combined with other modules to creat an application

import { NgModule } from '@angular/core';
@NgModule({

  imports: []->imports makes the exported declarations of other modules available in the current module,
  declarations: []-> all the components, directives, pipes part of the module,
  bootstrap: [],
  exports:[] -> services and components that can be used by other modules that import this module,
  providers:[]-> all the services that are part of the module

})
export class AppModule { }
______________________________________

LazyLoading: Lazy loading is a design pattern used to defer the initialization of modules until they are needed
it is a strategy used to reduce the time to interactive of a single page application.

when an application loads, all the modules are downloaded from the server including the lazy loaded modules
all the modules except the lazy loaded modules are combined together and rendered on the page
the lazy loaded modules are loaded to the page only when they are needed by requesting the cache.

you create a parent route pointing to the feature module and inside every feature module
you mention the components that should be loaded when the feature module is loaded

Lazy loading does not decrease the overall size of your app; it decreases the number of packets, or chunks, that must be loaded before the initial page becomes usable

import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './core/home/home.component';

const routes: Routes = [
  {
    path: 'profile', 
    loadChildren: () => import('./profile/profile.module').then(m => m.ProfileModule)
  },
  {
    path: 'product', 
    loadChildren: () => import('./product/product.module').then(m => m.ProductModule)
  },
  { path: '', component: HomeComponent, pathMatch: 'full' },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }


import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { ProfileComponent } from './profile/profile.component';

const routes: Routes = [
  { path: '', component: ProfileComponent }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ProfileRoutingModule { }
______________________________________
Guards: interfaces provided by angular which allows us to control the access to a route 
based on the conditions provided in the implementation of the interface
all the guards should be added to the providers array in app module

Guard functions can return either a boolean or an Observable<boolean> or Promise<boolean> 
which resolves to a boolean at some point in the future.

types:
    CanActivate: prevents us from navigating to the component until the conditions in the canActivate() are satisfied
    the method should return a boolean or a boolean promise or a boolean observable. 

    CanActivateChild: this works similar to canActivate but it is used to control access to the child routes 
    so that you dont have to create a route guard for every child route.
    {
        path: 'dashboard',
        canActivate: [AuthGuard],
        canActivateChild: [AuthGuard],
        component: DashboardComponent,
        children: [
            { path: ':id', component: InfoComponent},
            { path: ':id/edit', component: EditInfoComponent}
        ] 
    }

    CanLoad: to control routing to a lazy loaded module and also prevent the lazy loaded module from being downloaded from cache
    if the conditions are not met then we use a canLoad routing guard. if we use a canActivate guard the module will be downloaded even if the routing is not successful.

    CanDeactivate: This route guard is used to prevent the user from navigating away from a route until a condition is satisfied.
    for example we cannot let a user navigate away from a page as long as his changes on the page are not saved.

    Resolve: this guard is used to load data for the component before it is loaded and the data can be accessed inside the application
    by subscribing to router.data
______________________________________
    template driven forms:
        default froms used with angular
        more html and less component code
        hard to unit test
    reactive forms:
        less html code and more component code
        more flexible and allows us to use custom validators and create complex forms
        allows us to add fields dynamically
        easy to uniitest

    formGroup: The form will be treated as a FormGroup in the component class, so the formGroup directive allows to give a name to the form group.
    ngSubmit: This is the event that will be triggered upon submission of the form.
    formControlName: Each form field should have a formControlName directive with a value that will be the name used in the component class.
    formBuilder: allows us to build forms using a json object instead of using individual formControl objects

    import { Component, OnInit } from '@angular/core';
    import { FormBuilder, FormGroup, Validators } from '@angular/forms';

    @Component({
        selector: 'app-root',
        templateUrl: './app.component.html',
        styleUrls: ['./app.component.css']
    })
    export class AppComponent implements OnInit {
        myForm: FormGroup;

        constructor(private fb: FormBuilder) {}

        ngOnInit() {
            this.myForm = this.fb.group({
                name: ['Sammy', Validators.required],
                email: ['', [Validators.required, Validators.email]],
                message: ['', [Validators.required, Validators.minLength(15)]],
            });
        }

        onSubmit(form: FormGroup) {
            console.log('Valid?', form.valid); // true or false
            console.log('Name', form.value.name);
            console.log('Email', form.value.email);
            console.log('Message', form.value.message);
        }
    }

    Form States:	
        Pristine:	The user has not modified the form control
        Dirty:	The user has modified the form control
        Touched:	The user has interacted with the form control, e.g., by clicking or focusing on it.
        Untouched:	The form control has not been interacted with by the user.
        Valid:	The form control's value meets the validation rules defined in the application.
        Invalid:	The form control's value does not meet the validation rules defined in the application.
______________________________________
life cycle methods: all components and directives have life cycle methods

    constructor(): called first it is not a hook or life cycle method it is a typescript feature

    ngOnChanges(changes: SimpleChanges): called once before ngOnInit and Invoked everytime there is a change in @Input() properties.
    using SimpleChanges object you get access to previous values and current values.

    ngOnInit():Invoked when the component is initialised. used for adding all the initialisation logic because we will not have all the @Input properties available while the constructor is run. this hook is called only once after the first ngOnChanges().

    ngDoCheck(): Invoked when change detector of the component is invoked. it allows us to implement our own change detection algorithm for the given component. Invoked immediately after ngOnInit() during initial load and after ngOnChange() in every change detection run.

    dont use onchange, docheck in same component as it may cause a infinite loop

    --the below 4 hooks are only for components--
        ngAfterContentInit(): invoked after angular performs any content projection into the child components view
        ngAfterContentChecked(): invoked after the content of the given component has been checked by change detection mechanism
        ngAfterViewInit(): invoked after the components view has been fully initialised
        ngAfterViewChecked(): invoked after the view of the given component has been checked by the change detection
    -- --

    ngOnDestroy(): invoked before the component is removed from the DOM and angular destroys the component add all the clean up logic in this method
______________________________________
Change Detection: is a mechanism that detects the changes in application state and sync it with application view
every component will have its own change detector class which eventually forms a tree of change detectors, when change detection is
triggered angular walks down this tree of change detectors to determine if any of them have reported changes.
Change detection starts from the node where the change is detected and runs down to all the child components

Strategies:
    default(checkAlways):
        angular checks for changes in all components in every change detection cycle, regardless of whether the component's data has actually changed or not.

    OnPush:
        with onPush Strategy, angular checks the component only if the inputs to the component has changed or if an event originated 
        from the component or is subtree

        import { Component, ChangeDetectionStrategy } from '@angular/core';
        @Component({
            selector: 'app-my-component',
            templateUrl: './my-component.component.html',
            styleUrls: ['./my-component.component.css'],
            changeDetection: ChangeDetectionStrategy.OnPush
        })
        export class MyComponent {}
    
    Detached:
        this strategy allows you to manually control when and how change detection is triggered for a component
        it completely disables change detection for the component and its subtree and you have to manually tigger change detection using the 'changeDetectorRef'
        To use the "Detached" strategy, you need to manually detach the component's change detector using the detach() method of the ChangeDetectorRef.

        import { Component, ChangeDetectorRef } from '@angular/core';
        @Component({
            selector: 'app-my-component',
            templateUrl: './my-component.component.html',
            styleUrls: ['./my-component.component.css']
        })
        export class MyComponent {
            constructor(private cdr: ChangeDetectorRef) {}

            detachChangeDetection(): void {
                this.cdr.detach();
            }
        }
______________________________________
Generics: helps us to write reusable classes, functions and interfaces that don't explicitly define the types they use.

    function func<T>(data:T):T{
        console.log(data);
    }

    interface UserData<X,Y> {
        name: X;
        rollNo: Y;
    }

    const user: UserData<string, number> = {
        name: "Ram",
        rollNo: 1
    }
______________________________________
signals: A signal is just a special type of variable that holds a value. But unlike other variables, a signal also provides notification when the variable value changes.
Signals provide more reactivity. Using signals gives us finer control over change detection, which can improve performance.

const x = signal(5);
const y = signal(3);
const z = computed(() => x() + y());
console.log(z()); // 8
x.set(10);
console.log(z()); // 13
______________________________________
Interceptors: An HTTP interceptor is an Angular service that intercepts HTTP requests and responses generated by the built-in HTTP client of the Angular framework.

By using an interceptor to change HTTP requests and responses in a single area, we may avoid redundant code and make our code more intelligible.

Angular Interceptor is built similarly to other services, but it must have an intercept function. You will always intercept the request and, 
if desired, follow it through to intercept the response.

import { Injectable } from '@angular/core';
import { HttpInterceptor, HttpEvent, HttpRequest, HttpHandler } from '@angular/common/http';
import { Observable } from 'rxjs';

    @Injectable()
    export class ExampleInterceptor implements HttpInterceptor {
        intercept(httpRequest: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
            //any alteration in httpRequest can be done here
            return next.handle(httpRequest);
        }
    }

    @NgModule({
        providers: [
            { 
                provide: HTTP_INTERCEPTORS, useClass: ExampleInterceptor, multi:true
            },
        ]
    })

example operations:
    setting headers
    adding a token to the request
    transforming the response
    logging
    error handling
    modifying request url
    cancel the request
______________________________________
ng-container: helps us to avoid adding unnnecessary divs to the DOM

ng-template: works with structural directives such as ngIf,ngSwitch,ngFor and will not be displayed by default
    <div *ngIf="login else temp">
        user logged in
    </div>
    <ng-template #temp>
        please login
    <ng-template>

ng-content: used to render html elements or data present in parent component in child component. 
the passed in data or elements will be displayed inside the place of <ng-content> placed in the child component.
parent html:
<child>
    <div>{{data}}</div>
</child>
child html:
<ng-content>
</ng-content>
______________________________________
observable: unicast, which means only one observer is allowed.
once the observer unsubscribes then the observable is destroyed.

subjects and behavioursubjects are multicast, which means they can have multiple subscribers and
the subject is not destroyed until all the observers unsubscribe

subject: streams new data that is generated once the subscriber is subscribed to it.
For Subject, we don't need to initial a value.
const mySubject = new Rx.Subject();

behaviourSubject: caches the last value that is emitted before the subscriber is first subscribed to it and then emits the new data that is coming in.
But whenever we declare BehaviorSubject we need to initialize a default value.
const mySubject = new Rx.BehaviorSubject('Hey now!');

ReplaySubject: it can cache up to a specified number of emissions. Any subscribers will get all the cached values upon subscription. When would you need this behavior? Honestly, I have not had any need for such behavior, except for the following case:
const mySubject = new Rx.ReplaySubject(2);

Async Subject: it is a kind of subject which pushes the last value to its subscribers upon marking it as completed.
only when it is marked complete then the value is pushed. the value will not be pushed on calling next

import { AsyncSubject } from 'rxjs' ;
const as$ = new AsyncSubject(); 
as$.subscribe((data) => { 
    console.log( 'Subscriber A: ' + data);
});
as$.next(Math.random()); 
as$.complete(); 

as$.subscribe((data) => {
    console.log( 'Subscriber B: ' + data);
});
as$.next(Math.random());
as$.next(Math.random());
as$.complete();

// Subscriber A: 0.38896475571548295
// Subscriber B: 0.38896475571548295
______________________________________
In Angular, both @HostListener and @HostBinding are decorators 
used to interact with the host element of a component. 

HostListener: used for listening to events on host element
  @HostListener('document:keydown', ['$event'])
  onKeyDown(event: KeyboardEvent) {
    console.log('Key pressed:', event.key);
  }

HostBinding: used for binding properties of the host element
  set a class property to the component: 
  @HostBinding('class') class = 'ratings__average';

  @HostBinding('style.backgroundColor')
  get backgroundColor() {
    return this.isActive ? 'red' : 'blue';
  }
______________________________________
AOT: the angular code is compiled into performant javascript code during the build stage and generates a set of static files.
this offers faster rendering, small bundle sizes and the compiled code is ready to be served by a web browser and can be executed 
directly by the browser.

JIT:this is an alternative to AOT and the angular code is compiled to js code in the browser on the fly. while the app is loading
to do this, the angular compiler needs to be bundled with the final bundle delivered to the browser.

IVY: this is the rendering engine introduced in angular 9 and it is responsible for transforming angular templates into executable code. it provides tree shaking capabilities allowing the removal of unused code during the build process, resulting in smaller bundle sizes. Ivy provides a feature of Angular elements which allows angular components to be used in non angular environments.

In summary, AOT and JIT refer to different compilation strategies, while Ivy is the underlying rendering engine in Angular that works with both AOT and JIT compilation. AOT offers pre-compiled, optimized code during the build process, while JIT compiles the templates at runtime. Ivy enhances performance, build times, and offers additional features in Angular applications.
______________________________________

ViewChild: used to access the children of the view, the children can be another component or a html element
ViewChildren : used to access multiple child components of the component while view child only returns the first occurence
    @ViewChild(JokeComponent) jokeViewChild: JokeComponent;
    @ViewChildren(JokeComponent) jokeViewChildren: QueryList<JokeComponent>;
    @ViewChild("header") headerEl: ElementRef;

ContentChild: used to access the content that has been projected by the parent content into the child component using <ng-content>
ContentChildren: used in the child component to access multiple child components that have been projected by the parent content into the child component using <ng-content>
    @ContentChild(JokeComponent) jokeContentChild: JokeComponent;

    @Component({
    selector: 'joke-list',
    template: `
                <h4 #header>View Jokes</h4>
                <joke *ngFor="let j of jokes" [joke]="j">
                    <span class="setup">{{ j.setup }}?</span>
                    <h1 class="punchline">{{ j.punchline }}</h1>
                </joke>
                <h4>Content Jokes</h4>
                <ng-content></ng-content>
            `
    })
    class JokeListComponent implements AfterViewInit {

        jokes: Joke[] = [
            new Joke("What did the cheese say when it looked in the mirror", "Hello-me (Halloumi)"),
            new Joke("What kind of cheese do you use to disguise a small horse", "Mask-a-pony (Mascarpone)")
        ];

        @ViewChild(JokeComponent) jokeViewChild: JokeComponent; 
        <!-- used to access the jokes component that is placed in the component as child component -->

        @ViewChildren(JokeComponent) jokeViewChildren: QueryList<JokeComponent>;
        @ViewChild("header") headerEl: ElementRef;

        @ContentChild(JokeComponent) jokeContentChild: JokeComponent; 
        <!-- used to access the jokes component that will be projected into this component by the app component -->

        constructor() {
            console.log(`new - jokeViewChild is ${this.jokeViewChild}`);
        }

        ngAfterViewInit() {
            console.log(`ngAfterViewInit - jokeViewChild is ${this.jokeViewChild}`);
        }
    }

    @Component({
        selector: 'app',
        template: `
                <joke-list>
                    <joke [joke]="joke"> (1)
                        <span class="setup">{{ joke.setup }}?</span>
                        <h1 class="punchline">{{ joke.punchline }}</h1>
                    </joke>
                </joke-list>
        `
    })
    class AppComponent {
        joke: Joke = new Joke("A kid threw a lump of cheddar at me", "I thought ‘That’s not very mature’");
    }
______________________________________

// We can see a clear pattern, will solve it recursively
const sum  = function (a) {
  return function (b) {
    if (b) {
      return sum(a+b); // it takes an argument and return a function which again can take an argument.
    }
    return a; // it will keep on adding 1+2+3+4..
  }
};
______________________________________
NgRX: Angular implementation of Redux supported by RxJS

State: State is a representation of the application
it can be user info, data from server, view/UI state

as the application grows in size, it gets difficult to manage multiple states and react to changes,
loosing predictibility and making it difficult to identify bugs.

Redux Principles:
    Single source of truth (store)
    State is read only
    all changes to state are made by pure functions (reducers)

Redux pattern:
    user -> action -> reducer -> new state

user dispatches an action which invokes a reducer

NgRx Libraries:

    @ngrx/store: the core library
    @ngrx/effects: used to handle side effects such as communication with back-end server
    @ngrx/router: used to the angular router to ngrx store
    @ngrx/entity: used to manage record collections
    @ngrx/store-devtools: allows us to inspect and debug the application state
    @ngrx/schematics: scaffolding library that provides CLI commands to generate files

______________________________________

Angular Dependency Injection:
 Module Injector:
    every service marked with {prvoideIn:root} and declared in the eagerly loaded module will be instanitated and provided
    by the angular module Injector. The module Injector has the following hierarchy

        NullInjector :
            ^
        Platform module
            ^
        Root Injector
            ^
        Child Injector
    
    services declared as part of the lazy loaded modules are instantiated and provided by the child Injector
    
 Element Injector:
    This injector comes into picture when the service is declared in the providers array of the component
    this injector has the following structure
    
    Element Injector of Root Component
                ^
    Element Injector of Child component
                ^
    Element Injector of Grand Child component

    whenever a service instance is needed, the component will first look in its providers array and then go to providers if the parent
    component. If the instance is not found, then it goes to the Injector of module injector tree
______________________________________

forRoot: 

when you import a module A in a lazy loaded module B and a eagerly loaded module C, then the services provided in the module A
will be instantiated by the module Injector which is the root Injector as well as the child Injector of the lazy loaded module.
This will make multiple instances of the services available in the application. 
To avoid this, and to make a service singleTon we need to move its instaniation to the module injector we use
{
    providedIn: 'platform' | 'root' | null
}
based on the value provided it will be moved to respective Injector in module Injector hierarchy.
with this configuraton even if the service is inside a lazy loaded module it will be moved to the root Injector and will not be instantiated again

In earlier versions of angular before angular 7, we have to declare static forRoot and forFeature methods on the Module class

forChild:

when ever you want to have a different instance of a service to be availble for a child component, then we implement a static forChild method on the module class 
______________________________________
CommonModule : it is imported in every feature module that we create and it contains information about only few directives
BrowserModule: it is imported only once in the root module or app module which will be bootstraped hence it contains information
about the bootstraping as well along with common directives.
______________________________________
Resolver: resolver is basically the intermediate code which has been executed when a link has been clicked and 
before the component is loaded.
to create a resolver we implement the Resolve interface and override the resolve() it should return a value of 
return a observable. 

the resolved data can be accessed using the activatedRoute Object

const routes: Routes = [
  { path: 'home', component: HomeComponent },
  {
    path: 'products',
    component: ProductsComponent,
    resolve: { products: ProductsResolverService }
  },
  { path: 'about', component: AboutComponent }
];
export class ProductsComponent implements OnInit {
  products: Product[];
 
  constructor(private activatedRoute: ActivatedRoute) {}
 
  ngOnInit(): void {
    this.activatedRoute.data.subscribe((response: any) => {
      console.log('PRODUCT FETCHING', response);
      this.products = response.products;
      console.log('PRODUCT FETCHED');
    });
  }
}
______________________________________
Dependency Providers in Angular DI:

useClass - this option tells Angular DI to instantiate a provided class when a dependency is injected
useExisting - allows you to alias a token and reference any existing one.
useFactory - allows you to define a function that constructs a dependency. used to decide the dependency using the information which wouldn't be available until the runtime.
useValue - provides a static value that should be used as a dependency.

______________________________________
TreeShakable or dead code elimination:

elemination or removal of dead code. In an application there can be many modules that are imported and exported
using tree shaking the browser only loads the modules that are being used in the code. it ignores the modules that are not being
used any where in the code. it gets rid of unused dependencies and modules.
webpack uses a dependency graph to identify which modules are being used and which are not

we need to use export and import ES6 mdoule syntax
it doesnt work with common js syntax, so we need to disable the babel configuration
that converts ES6 into commonjs syntax

we also need to avoid side effects, because if a function has side effect code, it will be hard for
webpack to decide if it can be eliminated or not in the final code
______________________________________
