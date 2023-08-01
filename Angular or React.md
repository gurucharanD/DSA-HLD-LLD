Most of the time, both frameworks do the trick. Chose the framework that matches your team. If you like opinionated frameworks - i.e. frameworks that guide you - chose Angular. If you need a lot of freedom or if you don't like TypScript, chose React.

Small Angular applications have a surprisingly large memory footprint. So I'd prefer React for small things like Wordpress plugins. However, if you're writing a large application, memory and AFAIK even performance are in the same league.

Angular assumes it's owning the entire HTML page. So it's a bit difficult to embed Angular in an existing page, or to write microfrontends with Angular. But that's possible, too: just convert your Angular app into a webcomponent.

In any case, both frameworks are mature and have a huge community. The market share of React is larger, but if you're looking at the absolute download figures, both frameworks are popular and even growing.

You gave some clues by mentioning the old application. If your team has a strong Java background, they'll probably prefer Angular. Modern React encourages to abandon object-oriented programming in favor of functional programming. That's pretty cool, but if you're a long-term JSF programmer (like 10+ years), you're already busy learning HTML, CSS, and TypeScript. Maybe it's a bit much to add a new programming paradigm to the stack of stuff to learn. But again - every team is different. Let your team decide!