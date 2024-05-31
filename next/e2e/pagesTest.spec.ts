import { test, expect } from '@playwright/test';

test('VER-4 has "Hello World!" on homepage', async ({ page }) => {
  await page.goto('http://localhost:3000/');

  await expect(page.getByText('Hello world!')).toBeVisible()
});

test('VER-5 clicking on Test! link opens test page', async ({ page }) => {
  await page.goto('http://localhost:3000/');

  await page.getByRole('link', { name: 'Test!' }).click();

  await expect(page.getByText('This is a test page!')).toBeVisible();
});

test('VER-6 always fails', async ({ page }) => {
  await page.goto('http://localhost:3000/');
  await expect(page.getByText('This text does not and will not exist!')).toBeVisible();
})
