import { BrowserModule } from '@angular/platform-browser';
import { NgModule, importProvidersFrom } from '@angular/core';
import { provideHttpClient } from '@angular/common/http';
import { ReactiveFormsModule } from '@angular/forms';

// Components


// Modules
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { WordleSolverComponent } from './wordle-solver/wordle-solver.component';

// Services


@NgModule({
	declarations: [
		AppComponent,
		WordleSolverComponent
	],
	imports: [
		AppRoutingModule,
		BrowserModule,
		ReactiveFormsModule,
	],
	bootstrap: [AppComponent],
	providers: [provideHttpClient()]
})
export class AppModule {}