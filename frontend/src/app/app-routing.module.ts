import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule, Routes } from '@angular/router';

export const routes: Routes = [
	{ path: '', redirectTo: 'home', pathMatch: 'full' },
	{
		path: 'home',
		loadComponent: () =>
			import('./home/home.component').then(
				mod => mod.HomeComponent
			),
	},
    {
		path: 'wordle',
		loadComponent: () =>
			import('./wordle-solver/wordle-solver.component').then(
				mod => mod.WordleSolverComponent
			),
	}
];

@NgModule({
	imports: [CommonModule, RouterModule.forRoot(routes)],
	exports: [RouterModule],
	declarations: [],
})
export class AppRoutingModule {}