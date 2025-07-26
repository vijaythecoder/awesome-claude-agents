# Tailwind CSS Frontend Expert - Usage Examples

This guide demonstrates various ways to use the `tailwind-frontend-expert` agent for common frontend development tasks.

## Table of Contents

1. [Basic Component Creation](#basic-component-creation)
2. [Responsive Design](#responsive-design)
3. [Dark Mode Implementation](#dark-mode-implementation)
4. [Component Refactoring](#component-refactoring)
5. [Animation and Transitions](#animation-and-transitions)
6. [Form Styling](#form-styling)
7. [Performance Optimization](#performance-optimization)
8. [Framework Integration](#framework-integration)

## Basic Component Creation

### Example 1: Simple Card Component

**Prompt:**
```
Create a product card component with an image, title, description, price, and add to cart button
```

**Expected Response:**
The agent will create a responsive card with proper Tailwind classes:

```html
<div class="max-w-sm rounded-lg overflow-hidden shadow-lg hover:shadow-xl transition-shadow duration-300 bg-white dark:bg-gray-800">
  <img class="w-full h-48 object-cover" src="/product-image.jpg" alt="Product name">
  <div class="p-6">
    <h3 class="font-bold text-xl mb-2 text-gray-900 dark:text-white">Product Title</h3>
    <p class="text-gray-700 dark:text-gray-300 text-base mb-4">
      This is a brief description of the product highlighting its key features.
    </p>
    <div class="flex items-center justify-between">
      <span class="text-2xl font-bold text-gray-900 dark:text-white">$99.99</span>
      <button class="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded-lg transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 dark:focus:ring-offset-gray-800">
        Add to Cart
      </button>
    </div>
  </div>
</div>
```

### Example 2: Navigation Bar

**Prompt:**
```
Build a responsive navigation bar with logo, menu items, and mobile hamburger menu
```

**Expected Response:**
The agent will create a fully responsive navigation with mobile support:

```html
<nav class="bg-white dark:bg-gray-900 shadow-lg">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex justify-between h-16">
      <div class="flex items-center">
        <!-- Logo -->
        <div class="flex-shrink-0 flex items-center">
          <img class="h-8 w-auto" src="/logo.svg" alt="Company">
        </div>
        
        <!-- Desktop Navigation -->
        <div class="hidden sm:ml-6 sm:flex sm:space-x-8">
          <a href="#" class="border-indigo-500 text-gray-900 dark:text-white inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium">
            Dashboard
          </a>
          <a href="#" class="border-transparent text-gray-500 dark:text-gray-300 hover:border-gray-300 hover:text-gray-700 dark:hover:text-white inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium">
            Team
          </a>
          <a href="#" class="border-transparent text-gray-500 dark:text-gray-300 hover:border-gray-300 hover:text-gray-700 dark:hover:text-white inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium">
            Projects
          </a>
        </div>
      </div>
      
      <!-- Mobile menu button -->
      <div class="flex items-center sm:hidden">
        <button type="button" class="inline-flex items-center justify-center p-2 rounded-md text-gray-400 hover:text-gray-500 hover:bg-gray-100 dark:hover:bg-gray-800 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-indigo-500">
          <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
          </svg>
        </button>
      </div>
    </div>
  </div>
  
  <!-- Mobile menu -->
  <div class="sm:hidden hidden" id="mobile-menu">
    <div class="pt-2 pb-3 space-y-1">
      <a href="#" class="bg-indigo-50 dark:bg-indigo-900 border-indigo-500 text-indigo-700 dark:text-indigo-200 block pl-3 pr-4 py-2 border-l-4 text-base font-medium">Dashboard</a>
      <a href="#" class="border-transparent text-gray-500 dark:text-gray-300 hover:bg-gray-50 dark:hover:bg-gray-800 hover:border-gray-300 hover:text-gray-700 dark:hover:text-white block pl-3 pr-4 py-2 border-l-4 text-base font-medium">Team</a>
      <a href="#" class="border-transparent text-gray-500 dark:text-gray-300 hover:bg-gray-50 dark:hover:bg-gray-800 hover:border-gray-300 hover:text-gray-700 dark:hover:text-white block pl-3 pr-4 py-2 border-l-4 text-base font-medium">Projects</a>
    </div>
  </div>
</nav>
```

## Responsive Design

### Example 3: Responsive Grid Layout

**Prompt:**
```
Create a responsive grid that shows 1 column on mobile, 2 on tablet, and 3 on desktop
```

**Expected Response:**
```html
<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 lg:gap-6 p-4 lg:p-6">
  <!-- Grid items -->
  <div class="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
    <h3 class="text-lg font-semibold mb-2">Item 1</h3>
    <p class="text-gray-600 dark:text-gray-400">Content goes here</p>
  </div>
  <!-- Repeat for more items -->
</div>
```

## Dark Mode Implementation

### Example 4: Dark Mode Toggle Component

**Prompt:**
```
Create a dark mode toggle switch with sun and moon icons
```

**Expected Response:**
```html
<button 
  type="button"
  class="relative inline-flex items-center h-6 rounded-full w-11 transition-colors focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 dark:focus:ring-offset-gray-900"
  :class="darkMode ? 'bg-indigo-600' : 'bg-gray-200'"
  @click="darkMode = !darkMode"
>
  <span class="sr-only">Toggle dark mode</span>
  <span
    class="inline-block w-4 h-4 transform transition-transform bg-white rounded-full shadow-lg"
    :class="darkMode ? 'translate-x-6' : 'translate-x-1'"
  >
    <!-- Sun icon for light mode -->
    <svg v-if="!darkMode" class="w-3 h-3 text-yellow-500 absolute inset-0.5" fill="currentColor" viewBox="0 0 20 20">
      <path fill-rule="evenodd" d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z" clip-rule="evenodd" />
    </svg>
    <!-- Moon icon for dark mode -->
    <svg v-else class="w-3 h-3 text-indigo-600 absolute inset-0.5" fill="currentColor" viewBox="0 0 20 20">
      <path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z" />
    </svg>
  </span>
</button>
```

## Component Refactoring

### Example 5: Refactor Inline Styles to Tailwind

**Prompt:**
```
Refactor this component to use Tailwind classes instead of inline styles:
<div style="background-color: #f3f4f6; padding: 20px; border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
  <h2 style="color: #1f2937; font-size: 24px; margin-bottom: 10px;">Title</h2>
  <p style="color: #6b7280; line-height: 1.5;">Description text</p>
</div>
```

**Expected Response:**
```html
<div class="bg-gray-100 p-5 rounded-lg shadow">
  <h2 class="text-gray-800 text-2xl mb-2.5">Title</h2>
  <p class="text-gray-500 leading-relaxed">Description text</p>
</div>
```

## Animation and Transitions

### Example 6: Animated Dropdown Menu

**Prompt:**
```
Create a dropdown menu with smooth animation on open/close
```

**Expected Response:**
```html
<!-- Using Alpine.js for interactivity -->
<div class="relative" x-data="{ open: false }">
  <button 
    @click="open = !open"
    class="flex items-center space-x-2 text-gray-700 dark:text-gray-200 bg-white dark:bg-gray-800 px-4 py-2 rounded-lg shadow hover:shadow-md transition-shadow duration-200 focus:outline-none focus:ring-2 focus:ring-blue-500"
  >
    <span>Options</span>
    <svg class="w-4 h-4 transition-transform duration-200" :class="open ? 'rotate-180' : ''" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
    </svg>
  </button>
  
  <div 
    x-show="open"
    x-transition:enter="transition ease-out duration-200"
    x-transition:enter-start="opacity-0 transform scale-95"
    x-transition:enter-end="opacity-100 transform scale-100"
    x-transition:leave="transition ease-in duration-150"
    x-transition:leave-start="opacity-100 transform scale-100"
    x-transition:leave-end="opacity-0 transform scale-95"
    @click.away="open = false"
    class="absolute right-0 mt-2 w-48 rounded-lg shadow-lg bg-white dark:bg-gray-800 ring-1 ring-black ring-opacity-5"
  >
    <div class="py-1">
      <a href="#" class="block px-4 py-2 text-sm text-gray-700 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-700">Option 1</a>
      <a href="#" class="block px-4 py-2 text-sm text-gray-700 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-700">Option 2</a>
      <a href="#" class="block px-4 py-2 text-sm text-gray-700 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-700">Option 3</a>
    </div>
  </div>
</div>
```

## Form Styling

### Example 7: Complete Form with Validation States

**Prompt:**
```
Create a contact form with inputs for name, email, message, and validation states
```

**Expected Response:**
```html
<form class="max-w-lg mx-auto p-6 bg-white dark:bg-gray-800 rounded-lg shadow-lg">
  <h2 class="text-2xl font-bold mb-6 text-gray-900 dark:text-white">Contact Us</h2>
  
  <!-- Name Field -->
  <div class="mb-4">
    <label for="name" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
      Name
    </label>
    <input 
      type="text" 
      id="name" 
      name="name"
      class="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:text-white"
      placeholder="John Doe"
    >
  </div>
  
  <!-- Email Field with Error State -->
  <div class="mb-4">
    <label for="email" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
      Email
    </label>
    <input 
      type="email" 
      id="email" 
      name="email"
      class="w-full px-3 py-2 border border-red-300 rounded-md shadow-sm focus:ring-red-500 focus:border-red-500 dark:bg-gray-700 dark:text-white"
      placeholder="john@example.com"
    >
    <p class="mt-1 text-sm text-red-600 dark:text-red-400">Please enter a valid email address</p>
  </div>
  
  <!-- Message Field -->
  <div class="mb-6">
    <label for="message" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
      Message
    </label>
    <textarea 
      id="message" 
      name="message"
      rows="4"
      class="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:text-white resize-none"
      placeholder="Your message here..."
    ></textarea>
  </div>
  
  <!-- Submit Button -->
  <button 
    type="submit"
    class="w-full bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded-md transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 dark:focus:ring-offset-gray-800"
  >
    Send Message
  </button>
</form>
```

## Performance Optimization

### Example 8: Optimize Component with Too Many Classes

**Prompt:**
```
Optimize this component that has redundant Tailwind classes:
<div class="flex flex-row items-center justify-center align-middle flex items-center p-4 p-6 m-2 m-4 bg-white bg-gray-100">
```

**Expected Response:**
The agent will identify and remove redundant classes:

```html
<!-- Optimized version -->
<div class="flex items-center justify-center p-6 m-4 bg-gray-100">
  <!-- Removed redundant: flex-row (default), align-middle (use items-center), duplicate flex, duplicate items-center, p-4 (overridden by p-6), m-2 (overridden by m-4), bg-white (overridden by bg-gray-100) -->
</div>
```

## Framework Integration

### Example 9: React Component with Tailwind

**Prompt:**
```
Create a React button component that accepts variant props (primary, secondary, danger) with Tailwind styling
```

**Expected Response:**
```jsx
import React from 'react';
import clsx from 'clsx';

const Button = ({ children, variant = 'primary', disabled = false, onClick, className, ...props }) => {
  const baseClasses = 'px-4 py-2 rounded-lg font-medium transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-offset-2';
  
  const variantClasses = {
    primary: 'bg-blue-600 hover:bg-blue-700 text-white focus:ring-blue-500',
    secondary: 'bg-gray-200 hover:bg-gray-300 text-gray-800 focus:ring-gray-500',
    danger: 'bg-red-600 hover:bg-red-700 text-white focus:ring-red-500'
  };
  
  const disabledClasses = 'opacity-50 cursor-not-allowed';
  
  return (
    <button
      className={clsx(
        baseClasses,
        variantClasses[variant],
        disabled && disabledClasses,
        className
      )}
      disabled={disabled}
      onClick={onClick}
      {...props}
    >
      {children}
    </button>
  );
};

export default Button;

// Usage:
// <Button variant="primary">Click me</Button>
// <Button variant="danger" disabled>Delete</Button>
```

### Example 10: Vue 3 Component with Tailwind

**Prompt:**
```
Create a Vue 3 modal component with Tailwind CSS and transition effects
```

**Expected Response:**
```vue
<template>
  <Teleport to="body">
    <Transition name="modal">
      <div 
        v-if="isOpen" 
        class="fixed inset-0 z-50 flex items-center justify-center p-4"
        @click.self="closeModal"
      >
        <!-- Backdrop -->
        <div class="absolute inset-0 bg-black bg-opacity-50"></div>
        
        <!-- Modal -->
        <div class="relative bg-white dark:bg-gray-800 rounded-lg shadow-xl max-w-md w-full max-h-[90vh] overflow-hidden">
          <!-- Header -->
          <div class="flex items-center justify-between p-4 border-b dark:border-gray-700">
            <h3 class="text-lg font-semibold text-gray-900 dark:text-white">
              {{ title }}
            </h3>
            <button 
              @click="closeModal"
              class="text-gray-400 hover:text-gray-500 dark:hover:text-gray-300 focus:outline-none"
            >
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </div>
          
          <!-- Body -->
          <div class="p-4 overflow-y-auto max-h-[60vh]">
            <slot></slot>
          </div>
          
          <!-- Footer -->
          <div class="flex justify-end space-x-2 p-4 border-t dark:border-gray-700">
            <button 
              @click="closeModal"
              class="px-4 py-2 text-gray-700 dark:text-gray-300 bg-gray-200 dark:bg-gray-700 rounded-lg hover:bg-gray-300 dark:hover:bg-gray-600 transition-colors"
            >
              Cancel
            </button>
            <button 
              @click="confirmAction"
              class="px-4 py-2 text-white bg-blue-600 rounded-lg hover:bg-blue-700 transition-colors"
            >
              Confirm
            </button>
          </div>
        </div>
      </div>
    </Transition>
  </Teleport>
</template>

<script setup>
import { defineProps, defineEmits } from 'vue';

const props = defineProps({
  isOpen: {
    type: Boolean,
    required: true
  },
  title: {
    type: String,
    default: 'Modal Title'
  }
});

const emit = defineEmits(['close', 'confirm']);

const closeModal = () => {
  emit('close');
};

const confirmAction = () => {
  emit('confirm');
};
</script>

<style scoped>
.modal-enter-active,
.modal-leave-active {
  transition: opacity 0.3s ease;
}

.modal-enter-from,
.modal-leave-to {
  opacity: 0;
}

.modal-enter-active .relative,
.modal-leave-active .relative {
  transition: transform 0.3s ease;
}

.modal-enter-from .relative {
  transform: scale(0.9);
}

.modal-leave-to .relative {
  transform: scale(0.9);
}
</style>
```

## Tips for Using the Agent

1. **Be Specific**: The more specific your request, the better the output
2. **Mention Frameworks**: If using React, Vue, etc., mention it in your prompt
3. **Request Variants**: Ask for different states (hover, focus, disabled) when needed
4. **Dark Mode**: Specify if you want dark mode support included
5. **Responsive Requirements**: Mention specific breakpoint needs
6. **Accessibility**: Request ARIA labels and keyboard navigation when needed

## Advanced Usage

### Combining with Other Agents

You can combine the Tailwind agent with other specialized agents:

```bash
# First, use the Tailwind agent for styling
> Use the tailwind-frontend-expert to create a data table component

# Then, use a React specialist for logic
> Use the react-architect to add sorting and filtering logic to this table
```

### Iterative Refinement

```bash
# Initial request
> Create a pricing card component

# Refinement
> Add a "Most Popular" badge and animate it

# Further refinement
> Make it fully responsive and add dark mode support
```

The Tailwind CSS Frontend Expert agent is designed to understand context and build upon previous work, making iterative development smooth and efficient.