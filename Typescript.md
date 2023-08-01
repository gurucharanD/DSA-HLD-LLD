Never vs Unknown:

 never represents the absence of any possible value,
 unknown represents a value of an unknown type that requires type checking before use.
 never is typically used in scenarios where a certain condition will never occur
 unknown is used when dealing with uncertain or dynamically typed data that needs to be checked before handling.
______________________________________
Declare Keyword:

used to tell the compiler about the types and symbols that are defined in external JavaScript libraries or environments. 
It is a way to inform the compiler about existing code that is written in JavaScript without providing the implementation details. 

Type Definitions for JavaScript Libraries:
    When using JavaScript libraries that do not have their own TypeScript definitions, you can use the declare keyword to create declarations for the types, functions, classes, or objects provided by those libraries. This allows the TypeScript compiler to understand the types and provide type checking and autocompletion support. 

    declare module 'library-name' {
        export function someFunction(arg: string): void;
        export class SomeClass {
            // class members
        }
    }

Global Variables and Objects: 
    If your code relies on global variables or objects that are defined externally, you can use the declare keyword to inform TypeScript about their existence. This prevents TypeScript from raising undeclared variable errors. 

    declare const globalVariable: string;
    declare const globalObject: {
        property1: number;
        property2: string;
    };
______________________________________
Partial: In TypeScript, the Partial<T> mapped type is a built-in utility type that allows you to create a new type with all properties of the original type T, but with each property marked as optional. It enables you to easily create a new type that represents a partial subset of another type. Here's an example:

interface User {
  id: number;
  name: string;
  email: string;
}

type PartialUser = Partial<User>;

// PartialUser is equivalent to:
// {
//   id?: number | undefined;
//   name?: string | undefined;
//   email?: string | undefined;
// }
______________________________________

Omit: In TypeScript, the Omit<T, K> utility type is used to create a new type that omits specified properties K from the original type T. It allows you to easily create a type that excludes certain properties, providing a convenient way to narrow down or remove properties from existing types. Here's an example:

interface User {
  id: number;
  name: string;
  email: string;
  age: number;
}

type UserWithoutEmail = Omit<User, 'email'>;

// UserWithoutEmail is equivalent to:
// {
//   id: number;
//   name: string;
//   age: number;
// }
______________________________________

Record: In TypeScript, the Record<K, T> utility type is used to create a new type where each property is defined by the keys of type K and the values of type T. It allows you to easily create an object type with specific keys and their corresponding value types. Here's an example:

type MyRecord = Record<string, number>;

// MyRecord is equivalent to:
// {
//   [key: string]: number;
// }
______________________________________
Namespace vs Module:

Namespaces are essentially a way to group related code into a single global namespace. They are useful when you want to organize code within a single file or across multiple files, and when you want to prevent naming collisions between different parts of an application. Namespaces are also useful when defining a library or framework, as they provide a way to define a unique namespace for the library or framework's entities.

Modules, on the other hand, are a way to organize code into separate self-contained units that can be imported and used in other parts of an application. They are useful when you want to organize code across multiple files and directories, such as when defining separate components or features in an application. Modules are also useful for organizing related code that is used in multiple parts of an application, and for preventing naming collisions and other issues that can arise when working with large codebases.

In namespaces, all entities are defined in the global namespace, which can lead to naming collisions and other issues.
In modules, on the other hand, only the entities that are explicitly exported are added to the global namespace.

______________________________________
