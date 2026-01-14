import { render, screen } from '@testing-library/react';
import App from './App';

test('renders welcome message', () => {
  render(<App />);
  const welcomeElement = screen.getByText((content, element) => {
    return element?.tagName.toLowerCase() === 'h1' && content.startsWith('Welcome to');
  });
  expect(welcomeElement).toBeInTheDocument();
});
