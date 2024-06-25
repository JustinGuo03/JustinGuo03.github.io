import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { ReactiveFormsModule } from '@angular/forms';

// Components


// Modules
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { WordleSolverComponent } from './wordle-solver/wordle-solver.component';

// Services


@NgModule({
	declarations: [AppComponent],
	imports: [
		AppRoutingModule,
		BrowserModule,
		ReactiveFormsModule,

		//components
		WordleSolverComponent
	],
	bootstrap: [AppComponent],
})
export class AppModule {}